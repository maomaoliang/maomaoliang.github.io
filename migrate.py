#!/usr/bin/env python3
"""从 maomaoliang.github.io 静态站点提取文章，转换为 Hexo Markdown"""

import os
import re
import shutil
from pathlib import Path
from html.parser import HTMLParser
from html import unescape

STATIC_DIR = Path("/Users/xiaohan/Documents/logancode/maomaoliang.github.io")
HEXO_DIR = Path("/Users/xiaohan/Documents/logancode/maomaoliang-blog")
POSTS_DIR = HEXO_DIR / "source" / "_posts"
ASSETS_SRC = STATIC_DIR / "assets"
ASSETS_DST = HEXO_DIR / "source" / "assets"


class HTMLToMarkdown:
    """简单的 HTML 到 Markdown 转换器"""
    
    def convert(self, html: str) -> str:
        # 移除 headerlink 锚点
        html = re.sub(r'<a[^>]*class="headerlink"[^>]*>[^<]*</a>', '', html)
        
        # 处理标题 h1-h6
        for i in range(6, 0, -1):
            html = re.sub(
                rf'<h{i}[^>]*>(.*?)</h{i}>',
                lambda m, level=i: f'\n{"#" * level} {self._strip_tags(m.group(1)).strip()}\n',
                html, flags=re.DOTALL
            )
        
        # 处理图片
        html = re.sub(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*/?>',
                      r'![\2](\1)', html)
        html = re.sub(r'<img[^>]*src="([^"]*)"[^>]*/?>',
                      r'![](\1)', html)
        
        # 处理链接
        html = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
                      lambda m: f'[{self._strip_tags(m.group(2))}]({m.group(1)})',
                      html, flags=re.DOTALL)
        
        # 处理加粗和斜体
        html = re.sub(r'<strong>(.*?)</strong>', r'**\1**', html, flags=re.DOTALL)
        html = re.sub(r'<b>(.*?)</b>', r'**\1**', html, flags=re.DOTALL)
        html = re.sub(r'<em>(.*?)</em>', r'*\1*', html, flags=re.DOTALL)
        html = re.sub(r'<i>(.*?)</i>', r'*\1*', html, flags=re.DOTALL)
        
        # 处理代码块
        html = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>',
                      lambda m: f'\n```\n{unescape(self._strip_tags(m.group(1)))}\n```\n',
                      html, flags=re.DOTALL)
        
        # 处理行内代码
        html = re.sub(r'<code>(.*?)</code>', r'`\1`', html, flags=re.DOTALL)
        
        # 处理列表
        html = re.sub(r'<li>(.*?)</li>',
                      lambda m: f'- {self._strip_tags(m.group(1)).strip()}\n',
                      html, flags=re.DOTALL)
        html = re.sub(r'</?[ou]l[^>]*>', '\n', html)
        
        # 处理引用
        html = re.sub(r'<blockquote>(.*?)</blockquote>',
                      lambda m: '\n'.join(f'> {line}' for line in self._strip_tags(m.group(1)).strip().split('\n')),
                      html, flags=re.DOTALL)
        
        # 处理段落和换行
        html = re.sub(r'<br\s*/?>', '\n', html)
        html = re.sub(r'<p>(.*?)</p>',
                      lambda m: f'\n{m.group(1).strip()}\n',
                      html, flags=re.DOTALL)
        
        # 处理 <!-- more --> 标记
        html = re.sub(r'<a\s+id="more"\s*>\s*</a>', '\n<!-- more -->\n', html)
        
        # 清除剩余 HTML 标签
        html = re.sub(r'</?(?:div|span|section|figure|figcaption|table|thead|tbody|tr|td|th|hr)[^>]*>', '\n', html)
        html = re.sub(r'<[^>]+>', '', html)
        
        # 清理多余空行
        html = unescape(html)
        html = re.sub(r'\n{3,}', '\n\n', html)
        
        return html.strip()
    
    def _strip_tags(self, html: str) -> str:
        return unescape(re.sub(r'<[^>]+>', '', html))


def extract_article(html_path: Path):
    """从 HTML 文件中提取文章信息"""
    content = html_path.read_text(encoding='utf-8')
    
    # 提取标题
    title_match = re.search(r'<h1 class="post-title"[^>]*>(.*?)</h1>', content, re.DOTALL)
    if not title_match:
        return None
    title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
    
    # 提取日期
    date_match = re.search(r'datetime="([^"]+)"', content)
    date = date_match.group(1) if date_match else ""
    
    # 提取分类
    categories = []
    cat_section = re.search(r'<span class="post-category"[^>]*>(.*?)</span>\s*</span>', content, re.DOTALL)
    if cat_section:
        cats = re.findall(r'<a[^>]*>([^<]+)</a>', cat_section.group(1))
        categories = [c.strip() for c in cats]
    
    # 提取标签
    tags = []
    tags_section = re.search(r'<div class="post-tags">(.*?)</div>', content, re.DOTALL)
    if tags_section:
        tag_list = re.findall(r'>#\s*([^<]+)</a>', tags_section.group(1))
        tags = [t.strip() for t in tag_list]
    
    # 提取正文
    body_match = re.search(r'<div class="post-body"[^>]*>(.*?)</div>\s*(?:</div>)?\s*(?:<footer|<div class="post-footer")', content, re.DOTALL)
    if not body_match:
        # 备选方案
        body_match = re.search(r'<div class="post-body"[^>]*>(.*?)<footer class="post-footer"', content, re.DOTALL)
    
    body_html = body_match.group(1) if body_match else ""
    
    converter = HTMLToMarkdown()
    body_md = converter.convert(body_html)
    
    return {
        'title': title,
        'date': date,
        'categories': categories,
        'tags': tags,
        'body': body_md,
    }


def generate_front_matter(article: dict) -> str:
    """生成 Hexo front matter"""
    lines = ['---']
    lines.append(f'title: "{article["title"]}"')
    lines.append(f'date: {article["date"]}')
    if article['categories']:
        lines.append('categories:')
        for cat in article['categories']:
            lines.append(f'  - {cat}')
    if article['tags']:
        lines.append('tags:')
        for tag in article['tags']:
            lines.append(f'  - {tag}')
    lines.append('---')
    return '\n'.join(lines)


def main():
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 复制 assets 目录
    if ASSETS_SRC.exists() and not ASSETS_DST.exists():
        shutil.copytree(ASSETS_SRC, ASSETS_DST)
        print(f"✅ 复制 assets 目录: {ASSETS_SRC} -> {ASSETS_DST}")
    
    # 查找所有文章 HTML
    articles_found = 0
    for year_dir in sorted(STATIC_DIR.glob("[0-9]*")):
        for html_file in sorted(year_dir.rglob("index.html")):
            article = extract_article(html_file)
            if not article:
                print(f"⚠️  跳过 (无法解析): {html_file}")
                continue
            
            # 生成文件名（用标题，替换特殊字符）
            safe_title = re.sub(r'[/\\:*?"<>|]', '-', article['title'])
            safe_title = re.sub(r'\s+', '-', safe_title)
            md_file = POSTS_DIR / f"{safe_title}.md"
            
            front_matter = generate_front_matter(article)
            md_content = f"{front_matter}\n\n{article['body']}\n"
            
            md_file.write_text(md_content, encoding='utf-8')
            articles_found += 1
            print(f"✅ {article['title']} ({article['date'][:10]})")
    
    print(f"\n🎉 迁移完成！共 {articles_found} 篇文章")
    print(f"   文章目录: {POSTS_DIR}")


if __name__ == "__main__":
    main()
