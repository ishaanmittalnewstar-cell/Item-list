from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store specific items
items_list = ["Example Item 1", "Example Item 2"]

# HTML and CSS template stored as a Python string variable
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>8-D CHOIR SONGS</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; color: #333; }
        .container { max-width: 500px; background: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h2 { border-bottom: 2px solid #ddd; padding-bottom: 10px; }
        form { margin-bottom: 20px; display: flex; gap: 10px; }
        input[type="text"] { flex: 1; padding: 10px; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; color: white; }
        .btn-add { background-color: #28a745; }
        .btn-remove { background-color: #dc3545; padding: 5px 10px; font-size: 12px; }
        ul { list-style: none; padding: 0; }
        li { display: flex; justify-content: space-between; align-items: center; background: #f8f9fa; padding: 10px; margin-bottom: 8px; border-radius: 4px; border: 1px solid #eee; }
        .credit { position: fixed; right: 16px; bottom: 12px; font-size: 13px; color: #354BF0; background: rgba(255, 255, 255, 0.85); padding: 6px 10px; border-radius: 6px; }
    </style>
</head>
<body>

<div class="container">
    <h2>Add songs here</h2>

    <!-- Form to Add Items -->
    <form action="{{ url_for('add_item') }}" method="POST">
        <input type="text" name="item" placeholder="Enter here" required autocomplete="off">
        <button type="submit" class="btn-add">Add Item</button>
    </form>

    <!-- List to Display and Remove Items -->
    <ul>
        {% for item in items %}
        <li>
            <span>{{ item }}</span>
            <!-- Form to Remove a Single Item via its list index -->
            <form action="{{ url_for('remove_item', item_index=loop.index0) }}" method="POST" style="margin: 0;">
                <button type="submit" class="btn-remove">Remove</button>
            </form>
        </li>
        {% else %}
        <li style="color: #888;">No songs found</li>
        {% endfor %}
    </ul>
</div>

<div class="credit">Made by Ishaan</div>

</body>
</html>
"""

@app.route('/')
def index():
    # Renders the HTML directly from the Python string variable
    return render_template_string(HTML_TEMPLATE, items=items_list)

@app.route('/add', methods=['POST'])
def add_item():
    new_item = request.form.get('item')
    if new_item and new_item.strip():
        items_list.append(new_item.strip())
    return redirect(url_for('index'))

@app.route('/remove/<int:item_index>', methods=['POST'])
def remove_item(item_index):
    if 0 <= item_index < len(items_list):
        items_list.pop(item_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
