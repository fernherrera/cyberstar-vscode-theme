class Markup:
    """Define token scope categories"""

    # HTML
    variables = ["support.variable.liquid", "support.class.liquid"]
    tags = [
        "text.html.basic entity.name",
        "source.js-ignored-vscode",
        "entity.name.tag",
        # BLADE
        "meta.embedded.block.blade constant.other.php",
        "meta.embedded.block.blade keyword.operator.comparison.php",
        "meta.embedded.block.blade keyword.operator.arithmetic.php",
        "meta.tag.start.svelte keyword.control.svelte",
        "meta.tag.end.svelte keyword.control.svelte",
    ]
    tagsPunctuation = [
        "meta.tag.sgml.doctype.html",
        "punctuation.definition.tag",
        "meta.tag.block.any",
        "meta.tag.block.any.html",
        "meta.tag.inline.any",
        "source.css-ignored-vscode",
        "meta.tag.metadata.style.end.html",
        "text.html.vue invalid.illegal.character-not-allowed-here.html",
        "meta.tag.inline.i.start.html",
        "meta.tag.structure.div.start.html",
        "punctuation.definition.tag.end.html.vue",
        "invalid.illegal.character-not-allowed-here.html",
    ]
    attributes = [
        "entity.other.attribute-name",
        "entity.name.tag.liquid",
        "invalid.deprecated.entity.other.attribute-name",
        # BLADE
        "meta.embedded.block.blade storage.type.php",
    ]

    # MARKDOWN
    mdCode = [
        "markup.inline.raw.string.markdown",
        "punctuation.definition.raw.markdown",
        "markup.fenced_code.block.markdown",
        "markup.fenced_code.block.markdown punctuation",
        "markup.raw.block.markdown",
    ]
    mdCodeLanguage = ["fenced_code.block.language"]
    mdList = ["punctuation.definition.list.begin"]
    mdListPunctuation = ["punctuation.definition.list.begin"]
    mdHeading = ["entity.name.section", "markup.heading.setext"]
    mdHeadingPunctuation = ["punctuation.definition.heading"]
    mdLink = ["markup.underline.link", "markup.underline.link.image"]
    mdItalic = ["markup.italic", "punctuation.definition.italic"]
    mdBold = ["markup.bold", "punctuation.definition.bold"]
    mdStriked = [
        "markup.strikethrough",
        "punctuation.definition.strikethrough",
    ]
    mdQuote = [
        "markup.quote",
        "markup.quote.markdown punctuation.definition.quote.begin",
    ]
    mdQuotePunctuation = ["punctuation.definition.quote.begin"]
    component = [
        "entity.name.tag.other.html",
        "entity.name.tag support.class.component",
        "support.class.component.html",
    ]
    frontMatter = [
        "meta.embedded.block.frontmatter punctuation.definition.tag.begin",
        "meta.embedded.block.frontmatter punctuation.definition.tag.end",
        "meta.embedded.block.frontmatter string.unquoted.plain.out",
    ]

    # DIFF/PATCH
    diffAdd = [
        "source.diff meta.diff.header.to-file",
        "source.diff markup.inserted.diff",
        "source.diff punctuation.definition.to-file.diff",
        "source.diff punctuation.definition.inserted.diff",
    ]
    diffDel = [
        "source.diff punctuation.definition.from-file.diff",
        "source.diff meta.diff.header.from-file",
        "source.diff markup.deleted.diff",
        "source.diff punctuation.definition.deleted.diff",
    ]
    diffHead = ["source.diff meta.diff.header.command"]
    diffRange = [
        "source.diff punctuation.definition.range.diff",
        "source.diff meta.diff.range.unified",
    ]
