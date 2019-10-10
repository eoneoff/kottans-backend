const {Node} = require("node");

module.exports = class Stack {
    constructor() {
        this._root = null;
        this._length = 0;
    }

    push(value) {
        this._root = new Node(value, this._root);
        this._length++;
    }

    pop() {
        if (this._length) {
            const out = this._root.value;
            this._root = (this._root || {}).next;
            this._length--;
            return out;
        }
    }

    get length() {
        return this._length;
    }
};