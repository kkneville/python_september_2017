var Node = require('./node').Node;

function LinkedList(){
	this._length = 0;
	this.head = null;
	this.tail = null;
}
// look up prototype
LinkedList.prototype = {
	add: function (value) {
		var node = new Node(value);

		if (!this.head){
			this.head = node;
			this.tail = node;
			this._length++;

			return node;
		}

		this.tail.next = node;

		node.previous = tail;

		this.tail = node;

		this._length++;





}