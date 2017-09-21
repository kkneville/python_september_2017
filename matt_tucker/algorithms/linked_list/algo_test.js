var Queue = function() {
    this.head = null;

    this.enqueue = function(value) {
        console.log(value);
    }
}

var q = new Queue();

q.enqueue(6);

