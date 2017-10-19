var types_module = require('./data-types').dataTypes;
var LinkedList = types_module.LinkedList;

var linkedList = new LinkedList();

for (var i = 1; i <= 10; i++) {
    linkedList.add(i)
}

console.log(linkedList.to_array());

linkedList.remove(3);

console.log(linkedList.to_array());
