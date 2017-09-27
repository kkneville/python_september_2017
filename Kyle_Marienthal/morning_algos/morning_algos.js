function average(list){
	var avg = 0;
	var sum = 0;
	var runner = list.head
	var count = 0;
	while (runner){
		sum += count;
		count ++;
		runner = runner.next;
	}
	avg = sum/count;
	return avg;
}


function max(list){
	var runner = list.head;
	var max = list.val;
	while (runner){

	}
}

function findBack(pointer){
	this.head = pointer;
	this.val = value;
	runner = this.head;
	while(runner){
		if(runner.next == null){
			return runner.val;
		}
		runner = runner.next;
	}
}

function removeBack(list){
	head = list.head;
	list.val = value;
	runner = list.head;
	while(runner){
		if(runner.next.next == null){
			runner.next = null;
			return list;
		}
	}
	return list;
}

function max(list){
	var runner = list.head;
	var max = list.val;
	while(runner){
		if(runner.val > max){
			max = runner.val;
		}
		runner = runner.next;
	}
	return max;
}

// function min(node){
// 	var runner = node.head;
// 	var min = node.val;
// 	while(runner.next){
// 		if (runner.val < min){
// 			min = runner.next;
// 		}
// 		runner = runner.next;
// 	}
// 	return min;
// }

// function length(pointer){
// 	var runner = pointer;
// 	while (runner){
// 		runner = runner.next;
// 		count ++
// 	}
// 	return count
// }