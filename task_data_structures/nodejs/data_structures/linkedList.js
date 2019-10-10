const {Node} = require("node");

module.exports = class LinkedList {
    constructor() {
        this._root = null;
        this._length = 0;
    }

    *[Symbol.iterator]() {
        let current = this._root;
        while (current) {
            yield current;
            current = current.next;
        }
    }

    insert(value, successor = null) {
        if (successor && this._root.value != value) {
            for (let node of this) {
                if (node.next && node.next.value == successor) {
                    node.next = new Node(value, node.next);
                    this._length++;
                    return;
                }
            }
            throw Error(`Value ${value} is not in the list`);
        } else {
            this._root = new Node(value, this._root);
            this._length++;
        }
    }

    remove(value) {
        if (this._root.value == value) {
            this._root = this._root.next;
            this._length--;
        } else {
            for (let node of this) {
                if ((node.next || {}).value) {
                    node.next = node.next.next;
                    this._length--;
                    return;
                }
            }
            throw Error(`Value ${value} is not in the list`);
        }
    }

    show_list() {
        return Array.from(this, node => node.value);
    }

    get length() {
        return this._length;
    }
};