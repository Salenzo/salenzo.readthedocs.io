def on_page_markdown(markdown, page, config, files):
    if not page.is_homepage and page.file.src_uri.endswith("/index.md"):
        items = sorted(
            "- [%s](%s)"
            % (
                path[path.index("/") + 1 : path.rindex(".")],
                path[path.index("/") + 1 :],
            )
            for path in files.src_uris
            if "/" in path
            and path[: path.index("/")] == page.file.src_uri[:-9]
            and path != page.file.src_uri
        )
        if page.file.src_uri == "post/index.md":
            items = reversed(items)
        markdown += "\n\n" + "\n".join(items)
    return markdown