Assets/.                                # Main Asset Directory containing all USD files for the project
    Barrels/                            # Geometry folder identified by asset name
        Materials/                      # Folder containing USD file defining all materials used by the Asset.
            BarrelMaterials.usd (usda)  # Material USD file for all Barrels. *Optional as ASCII
        Textures/                       # Folder containing all Texture Maps. Directory per asset variation
            BarrelWithLid/              # Texture folder
            BarrelWithNoLid/            # Texture folder
            BarrelWithNoLid_v2/         # Texture folder
        BarrelsWithLid.usd (usdc)       # GeometryCache USD file. Save as crate. Variant Option
        BarrelsNoLid.usd (usdc)         # GeometryCache USD file. Save as crate. Variant Option
        BarrelsAsset.usd (usda)         # Reference in Barrel Geometry Variants. Optional save as ASCII
        Barrels.usd (usda)              # Reference in Assets and Materials. Optional save as ASCII. Variant Option
    