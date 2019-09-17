def v_request(obj):
    return True if ('name' in obj and 'price' in obj and 'isbn' in obj) else False

correct = {
    'name': 'hello',
    'price': 9.99,
    'isbn': 234543201242
}

incorrect = {
    'name': 'mike',
    'isbn': 234543201242
}