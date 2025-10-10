
class Styling:
    """Define token scope categories"""
    
    units = ["keyword.other.unit"]
    
    pseudoClasses = ["entity.other.attribute-name.pseudo-class"]
    
    pseudoElements = ["entity.other.attribute-name.pseudo-element"]
    
    classes = [
        "entity.other.attribute-name.class",
        "entity.other.attribute-name.class punctuation.definition.entity",
    ]
    
    suffix = [
      "entity.other.attribute-name.parent-selector-suffix punctuation.definition.entity",
    ]
    
    ids = [
        "source.css.scss entity.other.attribute-name.id ",
        "source.css entity.other.attribute-name.id ",
        "entity.other.attribute-name.id punctuation.definition.entity",
    ]
    
    reference = ["entity.name.tag.reference", "meta.property-list"]
    
    property = [
        "support.type.property-name.css",
        "support.type.vendored.property-name",
        "meta.property-list entity.name.tag.css",
        "meta.property-list.scss meta.property-list.scss entity.name.tag.css",
        "meta.property-list meta.property-name",
        "source.css.scss meta.property-list.scss entity.name.tag.css",
    ]
    
    value = [
        "support.constant.property-value",
        "support.constant.font-name",
        "meta.property-value.css",
        "meta.attribute.style.html",
    ]

    nums = ["constant.numeric"]
    
    tag = [
        "entity.name.tag.css",
        "meta.property-list.scss entity.name.tag.css",
    ]