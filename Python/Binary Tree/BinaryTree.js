import Node from './intro'

class BinaryTree{
    constructor() {
        this.root = null
    }

    insertAfter(node, data){
        if(node.left === null){
            node.left = new Node(data)
            return true
        } else if(node.right === null){
            node.right = new Node(data)
            return true
        }
        return false
    }

    insert(data){
        if(this.root){
            if(this.insertAfter(this.root, data)) return true
            else this.insertAfter(this.root.left, data)
        } else{
            this.root = new Node(data)
        }
    }
}