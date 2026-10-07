
from pyscript import display, document


def SKU_generator(e):
    document.getElementById('sku_output').innerHTML = ""

    category = document.getElementById('category').value
    product_name = document.getElementById('product_name').value
    stock_qty = document.getElementById('quantity').value

    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)

    display("SKU: " + sku, target='sku_output')


def create_order(e):

    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")

    subtotal = (
        float(prod1.value) * prod1.checked
        + float(prod2.value) * prod2.checked
        + float(prod3.value) * prod3.checked
        + float(prod4.value) * prod4.checked
        + float(prod5.value) * prod5.checked
    )


    tax_rate = 0.12
    tax = subtotal * tax_rate
    total = subtotal + tax


    receipt = """
    <h4>==== Receipt ====</h4>
    """

    if prod1.checked:
        receipt += f"<p>League of Legends Funko pops  ₱{float(prod1.value):.2f}</p>"
    if prod2.checked:
        receipt += f"<p>Gelato  ₱{float(prod2.value):.2f}</p>"

    if prod3.checked:
        receipt += f"<p>Dark Souls 3 (Deluxe) ₱{float(prod3.value):.2f}</p>"

    if prod4.checked:
        receipt += f"<p>Tiramisu (per slice)  ₱{float(prod4.value):.2f}</p>"

    if prod5.checked:
        receipt += f"<p>Jojo's Bizzare Adventure Part 7, Steel Ball Run (Per Vol)  ₱{float(prod5.value):.2f}</p>"


    if subtotal == 0:
        receipt += "<p>No items selected.</p>"


    receipt += f"""
    <hr>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>VAT (12%): ₱{tax:.2f}</p>
    <p><strong>Total: ₱{total:.2f}</strong></p>
    """


    document.getElementById("show").innerHTML = receipt