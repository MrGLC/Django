function createHashMap() {
  const myHashMap = new Map(); 

  // Add key-value pairs (keys can be of any data type):
  myHashMap.set("key1", "value1");
  myHashMap.set(20, "numberKey");
  myHashMap.set(true, "booleanKey");

  return myHashMap;
}

const myMap = createHashMap();
console.log(myMap.get(true)); // Output: "numberKey"
