const {Server} = require("./server/server");
const {LinkedList} = require("./data_structures/linkedList");

const list = new LinkedList();
list.insert(1);
list.insert(2);
list.insert(3);
new Server(list).run();