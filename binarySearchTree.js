function Node(data, left, right) {
  this.data = data;
  this.left = left;
  this.right = right;
}

function BST() {
  this.root = null;
  this.insert = insert;
  this.inOrder = inOrder;
  this.getMin = findMin;
  this.getMax = findMax;
  this.getHeight = findHeight;
  this.delete = deleteNode;
}

function insert(data) {
  var node = new Node(data, null, null);

  if(this.root == null) {
    this.root = node;
  } else {
    var current = this.root;
    var parent;

    while(true) {
      parent = current;
      if(data < current.data) {
        current = current.left;
        if(current == null) {
          parent.left = node;
          break;
        }
      } else {
        current = current.right;
        if(current == null) {
          parent.right = node;
          break;
        }
      }
    }
  }
}

function deleteNode(data) {
  var current = this.root;
  var parent;

  while(true) {
    if(data == current.data) {
      if(current.right === null && current.left === null) {
        current.data = null;
        return;
      }

      if(current.right === null || current.left === null){
        current.data = current.right.data || current.left.data;
        current.right = null;
        current.left = null;
        return;
      }

      current.data = current.right.data;
      current.left = current.right.left;
      current.right = current.right.right;

      break;
    } else if(data < current.data) {
      parent = current;
      current = current.left;

    } else {
      parent = current;
      current = current.right;
    }
  }
}

function inOrder(node) {
  if(node != null) {
    inOrder(node.left);
    console.log(node.show() + " ");
    inOrder(node.right);
  }
}

function preOrder(node) {
 if(node != null) {
   console.log(node.show() + " ");
   preOrder(node.left);
   preOrder(node.right);
 }
}

function postOrder(node) {
  if(node != null) {
    postOrder(node.left);
    postOrder(node.right);
    console.log(node.show() + " ");
  }
}

function findMin() {
  var current = this.root;
  while(current.left != null){
    current = current.left;
  }
  return current.data;
}

function findMax() {
  var current = this.root;
  while (current.right != null) {
    current = current.right;
  }
  return current.data;
}

// function findHeight(node) {
//   console.log(node.data);
//   if(node.left !== null) findHeight(node.left);
//   console.log('----' + node.data);
//   if(node.right !== null) findHeight(node.right);
//   console.log("====" + node.data);
//
// }

var num = new BST();
num.insert(23);
num.insert(5);
num.insert(45);
num.insert(3);
num.insert(12);
num.insert(26);
num.insert(99);
num.insert(80);
num.insert(110);
num.insert(70);
num.insert(90);
num.insert(1);
num.insert(13);
// inOrder(num.root);
// preOrder(num.root);
// postOrder(num.root);
// num.delete(45);
num.getHeight(num.root);