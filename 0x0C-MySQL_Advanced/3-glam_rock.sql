-- 3. Old school band
SELECT band_name, IFNULL(split, 2023) - formed  as lifespan from metal_bands WHERE style LIKE "%Glam rock%" ORDER BY lifespan DESC;