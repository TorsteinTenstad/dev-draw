from svg import SVG
import eliments

def get_next_mask_id():
    get_next_mask_id.id += 1
    return get_next_mask_id.id
get_next_mask_id.id = 0

def mask(eliment, mask):
    mask_id = get_next_mask_id()
    return f"""
<defs>
    <mask id="{mask_id}">
        {mask}

    </mask>
</defs>
<g mask = "url(#{mask_id})">
    {eliment}

</g>"""