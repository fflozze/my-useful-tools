import os
import json
import base64

def get_file_content(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def build_tree(path):
    name = os.path.basename(path)
    if os.path.isdir(path):
        # Skip hidden directories and specific ignored dirs
        if name.startswith('.') or name == '__pycache__':
            return None
            
        children = []
        try:
            entries = sorted(os.listdir(path))
        except OSError:
            return None
            
        for entry in entries:
            child_path = os.path.join(path, entry)
            child_node = build_tree(child_path)
            if child_node:
                children.append(child_node)
        
        # Only return directories if they have interesting content, or are the root
        if not children and name != 'useful_tools': 
             return None

        # Sort children: Directories first, then files
        children.sort(key=lambda x: (x['type'] != 'directory', x['name'].lower()))

        return {
            "name": name,
            "type": "directory",
            "children": children
        }
    else:
        # Only process markdown files
        if name.endswith('.md'):
            return {
                "name": name,
                "type": "file",
                "content": get_file_content(path)
            }
        return None

def generate_html(data):
    # Escape some chars for JS string injection if needed, 
    # but json.dumps handles most.
    json_data = json.dumps(data)
    
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Useful Tools Docs</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    
    <!-- Markdown & Highlight -->
    <script src="https://cdn.jsdelivr.net/npm/marked@11.2.0/marked.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/atom-one-dark.min.css">
    <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js"></script>
    <script>
        // Configure marked to add IDs to headings with French character support
        const renderer = {{
            heading(text, level, raw) {{
                const safeRaw = raw || text.replace(/<[^>]*>/g, '');
                const slug = safeRaw.toLowerCase().trim()
                    .replace(/[^\\w\\u00C0-\\u00FF]+/g, '-')
                    .replace(/^-+|-+$/g, '');
                return `<h${{level}} id="${{slug}}">${{text}}</h${{level}}>`;
            }}
        }};
        marked.use({{ renderer }});
    </script>
    
    <style>
        :root {{
            --bg-color: #0f172a;       /* Slate 900 */
            --sidebar-bg: #1e293b;    /* Slate 800 */
            --border-color: #334155;  /* Slate 700 */
            --text-primary: #f8fafc;  /* Slate 50 */
            --text-secondary: #94a3b8;/* Slate 400 */
            --accent-color: #38bdf8;  /* Sky 400 */
            --accent-hover: #0ea5e9;  /* Sky 500 */
            --item-hover: #334155;    /* Slate 700 */
            --code-bg: #1e293b;
        }}

        * {{ box-sizing: border-box; }}

        body {{
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            height: 100vh;
            background-color: var(--bg-color);
            color: var(--text-primary);
            overflow: hidden;
        }}

        /* --- Sidebar --- */
        #sidebar {{
            width: 320px;
            background-color: var(--sidebar-bg);
            border-right: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            flex-shrink: 0;
            transition: transform 0.3s ease;
        }}

        #sidebar-header {{
            padding: 24px;
            border-bottom: 1px solid var(--border-color);
        }}

        #sidebar-title {{
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 16px;
            letter-spacing: -0.025em;
        }}

        #search-container {{
            position: relative;
        }}

        #search-input {{
            width: 100%;
            padding: 10px 16px 10px 40px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            background-color: var(--bg-color);
            color: var(--text-primary);
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            outline: none;
            transition: border-color 0.2s;
        }}
        
        #search-input:focus {{
            border-color: var(--accent-color);
        }}

        #search-icon {{
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-secondary);
            width: 18px;
            height: 18px;
        }}

        #file-tree {{
            flex-grow: 1;
            overflow-y: auto;
            padding: 16px;
        }}

        /* Scrollbar styling */
        ::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        ::-webkit-scrollbar-track {{ background: transparent; }}
        ::-webkit-scrollbar-thumb {{
            background: #475569;
            border-radius: 3px;
        }}
        ::-webkit-scrollbar-thumb:hover {{ background: #64748b; }}

        /* --- Tree Items --- */
        .tree-item {{
            margin-bottom: 2px;
        }}

        .item-row {{
            display: flex;
            align-items: center;
            padding: 8px 12px;
            border-radius: 6px;
            cursor: pointer;
            color: var(--text-secondary);
            font-size: 0.95rem;
            transition: all 0.2s ease;
            user-select: none;
            text-decoration: none;
        }}

        .item-row:hover {{
            background-color: var(--item-hover);
            color: var(--text-primary);
        }}

        .item-row.active {{
            background-color: rgba(56, 189, 248, 0.1); /* Low opacity accent */
            color: var(--accent-color);
            font-weight: 500;
        }}

        .item-icon {{
            width: 20px;
            height: 20px;
            margin-right: 10px;
            flex-shrink: 0;
            opacity: 0.7;
        }}
        
        .folder-chevron {{
            width: 16px;
            height: 16px;
            margin-right: 4px;
            transition: transform 0.2s ease;
            opacity: 0.5;
        }}

        .folder.open > .item-row > .folder-chevron {{
            transform: rotate(90deg);
        }}

        .folder-content {{
            margin-left: 20px;
            border-left: 1px solid var(--border-color);
            overflow: hidden;
            display: none; /* Hidden by default */
            padding-left: 4px;
        }}
        
        .folder-content.open {{
            display: block;
            animation: slideDown 0.2s ease-out;
        }}

        @keyframes slideDown {{
            from {{ opacity: 0; transform: translateY(-5px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* --- Main Content --- */
        #main-content {{
            flex-grow: 1;
            overflow-y: auto;
            position: relative;
            background-color: var(--bg-color);
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 48px 40px;
        }}

        /* --- Markdown Styling --- */
        .markdown-body {{
            line-height: 1.7;
            font-size: 1.05rem;
        }}

        .markdown-body h1, .markdown-body h2, .markdown-body h3 {{
            color: var(--text-primary);
            font-weight: 600;
            margin-top: 2em;
            margin-bottom: 0.8em;
            letter-spacing: -0.02em;
        }}
        
        .markdown-body h1 {{ font-size: 2.5rem; border-bottom: 1px solid var(--border-color); padding-bottom: 0.3em; margin-top: 0; }}
        .markdown-body h2 {{ font-size: 1.75rem; }}
        .markdown-body h3 {{ font-size: 1.4rem; }}

        .markdown-body p {{
            margin-bottom: 1.25em;
            color: #cbd5e1; /* Slate 300 */
        }}

        .markdown-body a {{
            color: var(--accent-color);
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: border-color 0.2s;
        }}
        .markdown-body a:hover {{ border-bottom-color: var(--accent-color); }}

        .markdown-body strong {{ font-weight: 600; color: var(--text-primary); }}
        
        .markdown-body code {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9em;
            background-color: rgba(30, 41, 59, 0.6); /* Slate 800 with opacity */
            padding: 0.2em 0.4em;
            border-radius: 4px;
            color: #e2e8f0;
        }}

        .markdown-body pre {{
            background-color: var(--code-bg);
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            border: 1px solid var(--border-color);
            margin: 1.5em 0;
        }}

        .markdown-body pre code {{
            background-color: transparent;
            padding: 0;
            color: inherit;
        }}

        .markdown-body blockquote {{
            margin: 1.5em 0;
            padding: 0 1.5em;
            color: var(--text-secondary);
            border-left: 4px solid var(--border-color);
        }}

        .markdown-body ul, .markdown-body ol {{
            padding-left: 1.5em;
            margin-bottom: 1.25em;
        }}

        .markdown-body li {{
            margin-bottom: 0.5em;
        }}

        .markdown-body img {{
            max-width: 100%;
            border-radius: 8px;
            border: 1px solid var(--border-color);
        }}
        
        .markdown-body table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5em 0;
        }}
        
        .markdown-body th, .markdown-body td {{
            padding: 10px;
            border: 1px solid var(--border-color);
            text-align: left;
        }}
        
        .markdown-body th {{
            background-color: var(--sidebar-bg);
            font-weight: 600;
        }}

    </style>
</head>
<body>
    <div id="sidebar">
        <div id="sidebar-header">
            <div id="sidebar-title">Useful Tools</div>
            <div id="search-container">
                <svg id="search-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                <input type="text" id="search-input" placeholder="Search documentation...">
            </div>
        </div>
        <div id="file-tree"></div>
    </div>

    <div id="main-content">
        <div class="container">
            <div id="content-display" class="markdown-body">
                <div style="text-align: center; margin-top: 100px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#334155" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                    <h2 style="color: var(--text-secondary); padding-bottom: 0px; border-bottom: none;">Select a file to start</h2>
                    <p>Browser your documentation using the sidebar.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Icons SVG strings -->
    <script>
        const chevronRight = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>`;
        const folderIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>`;
        const fileIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path><polyline points="13 2 13 9 20 9"></polyline></svg>`;
        
        const fileData = {json_data};

        function renderTree(node, container, isRoot = false) {{
            if (!node) return;

            if (node.type === 'directory') {{
                const folderWrapper = document.createElement('div');
                folderWrapper.className = 'folder ' + (isRoot ? 'open' : ''); 
                
                // For the "header" of the folder
                const row = document.createElement('div');
                row.className = 'item-row';
                
                // If it's a folder, we need the chevron
                const chevronSpan = document.createElement('span');
                chevronSpan.className = 'folder-chevron';
                chevronSpan.innerHTML = chevronRight;
                row.appendChild(chevronSpan);
                
                const iconSpan = document.createElement('span');
                iconSpan.className = 'item-icon';
                iconSpan.innerHTML = folderIcon;
                row.appendChild(iconSpan);

                const textSpan = document.createElement('span');
                textSpan.textContent = node.name;
                row.appendChild(textSpan);

                // Click event to toggle
                row.onclick = (e) => {{
                    e.stopPropagation();
                    const content = folderWrapper.querySelector('.folder-content');
                    if (folderWrapper.classList.contains('open')) {{
                        folderWrapper.classList.remove('open');
                        content.classList.remove('open');
                    }} else {{
                        folderWrapper.classList.add('open');
                        content.classList.add('open');
                    }}
                }};

                folderWrapper.appendChild(row);

                // Container for children
                const contentDiv = document.createElement('div');
                contentDiv.className = 'folder-content ' + (isRoot ? 'open' : '');
                
                if (node.children) {{
                    node.children.forEach(child => {{
                        renderTree(child, contentDiv, false);
                    }});
                }}
                
                folderWrapper.appendChild(contentDiv);
                container.appendChild(folderWrapper);

            }} else if (node.type === 'file') {{
                const fileDiv = document.createElement('div');
                fileDiv.className = 'tree-item';
                fileDiv.dataset.name = node.name.toLowerCase(); // For search

                const row = document.createElement('div');
                row.className = 'item-row';
                
                // Spacer for where the chevron would be (16px + margin)
                const spacer = document.createElement('div');
                spacer.style.width = '20px';
                spacer.style.marginRight = '4px';
                row.appendChild(spacer);

                const iconSpan = document.createElement('span');
                iconSpan.className = 'item-icon';
                iconSpan.innerHTML = fileIcon;
                row.appendChild(iconSpan);

                const textSpan = document.createElement('span');
                textSpan.textContent = node.name.replace('.md', ''); // Clean name
                row.appendChild(textSpan);

                row.onclick = (e) => {{
                    e.stopPropagation();
                    // Clear active state
                    document.querySelectorAll('.item-row').forEach(el => el.classList.remove('active'));
                    row.classList.add('active');
                    
                    renderMarkdown(node.content);
                }};

                fileDiv.appendChild(row);
                container.appendChild(fileDiv);
            }}
        }}

        function renderMarkdown(content) {{
            const display = document.getElementById('content-display');
            const mainContent = document.getElementById('main-content');
            
            // Scroll to top when loading a new file
            mainContent.scrollTop = 0;
            
            display.innerHTML = marked.parse(content);
            hljs.highlightAll();
        }}
        
        // --- Search Logic ---
        const searchInput = document.getElementById('search-input');
        
        searchInput.addEventListener('input', (e) => {{
            const term = e.target.value.toLowerCase();
            const allFiles = document.querySelectorAll('.tree-item');
            const allFolders = document.querySelectorAll('.folder');

            if (term === '') {{
                // Reset visibility
                allFiles.forEach(el => el.style.display = 'block');
                allFolders.forEach(el => el.style.display = 'block');
                return;
            }}

            // Filter files
            allFiles.forEach(fileEl => {{
                const text = fileEl.innerText.toLowerCase();
                if (text.includes(term)) {{
                    fileEl.style.display = 'block';
                    // Walk up parents to unfold
                    let parent = fileEl.parentElement;
                    while(parent && parent.id !== 'file-tree') {{
                        if (parent.classList.contains('folder-content')) {{
                            parent.classList.add('open');
                            parent.parentElement.classList.add('open'); // The .folder wrapper
                        }}
                        parent = parent.parentElement;
                    }}
                }} else {{
                    fileEl.style.display = 'none';
                }}
            }});
            
            // Hide empty folders (optional optimization but keeps it clean)
            // A simple approach is just to let files show/hide. 
            // The folders will stay open if they have visible children.
        }});

        // --- Init ---
        const treeContainer = document.getElementById('file-tree');
        if (fileData && fileData.children) {{
             // We skip rendering the "useful_tools" root folder name itself, 
             // but render its contents directly into the sidebar
             // OR if you want to see "useful_tools" as a root folder, just:
             // renderTree(fileData, treeContainer, true);
             
             // Let's render children directly to make it "flat" at the top level
             fileData.children.forEach(child => renderTree(child, treeContainer, true));
        }}
    </script>
</body>
</html>
    """
    return html_template

def main():
    root_path = os.getcwd()
    print(f"Scanning directory: {root_path}")
    
    tree_data = build_tree(root_path)
    
    if not tree_data:
        print("No markdown files found or error scanning.")
        return

    html_content = generate_html(tree_data)
    
    output_file = 'index.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Successfully generated {output_file}")

if __name__ == "__main__":
    main()
