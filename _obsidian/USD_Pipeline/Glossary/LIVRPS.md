LIVRPS is an acronym for **Local, Inherits, VariantSets, References, Payload, Specializes**

1. **Local**:
    
    Iterate through all the layers in the local LayerStack looking for opinions on the PrimSpec at _path_ in each layer - recall that according to the definition of LayerStack, this is where the effect of direct opinions in all [SubLayers](https://openusd.org/release/glossary.html#usdglossary-sublayers) of the root layer of the LayerStack will be consulted. If no opinion is found, then…
    
2. **Inherits**:
    
    Resolve the [Inherits](https://openusd.org/release/glossary.html#usdglossary-inherits) affecting the prim at _path_, and iterate through the resulting targets. For each target, **recursively apply** **LIVRP** **evaluation** on the targeted LayerStack - **Note that the “S” is not present** - we ignore Specializes arcs while recursing . If no opinion is found, then…
    
3. **VariantSets**:
    
    Apply the resolved variant selections to all [VariantSets](https://openusd.org/release/glossary.html#usdglossary-variantset) that affect the PrimSpec at _path_ in the LayerStack, and iterate through the selected [Variants](https://openusd.org/release/glossary.html#usdglossary-variant) on each VariantSet. For each target, **recursively apply** **LIVRP** **evaluation** on the targeted LayerStack - **Note that the “S” is not present** - we ignore Specializes arcs while recursing. If no opinion is found, then…
    
4. **References**:
    
    Resolve the [References](https://openusd.org/release/glossary.html#usdglossary-references) affecting the prim at _path_, and iterate through the resulting targets. For each target, **recursively apply** **LIVRP** **evaluation** on the targeted LayerStack - **Note that the “S” is not present** - we ignore Specializes arcs while recursing. If no opinion is found, then…
    
5. **Payload**:
    
    Resolve the [Payload](https://openusd.org/release/glossary.html#usdglossary-payload) arcs affecting the prim at _path_; if _path_ has been **loaded on the stage,** iterate through the resulting targets just as we would references from step 4. If no opinion is found, then…
    
6. **Specializes**:
    
    Resolve the [Specializes](https://openusd.org/release/glossary.html#usdglossary-specializes) affecting the prim at _path_, and iterate through the resulting targets, **recursively applying *full* LIVRPS evaluation** on each target prim. If no opinion is found, then…
    
7. Indicate that we could find no authored opinion