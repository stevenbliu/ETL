db = db.getSiblingDB('mydatabase'); // Create and switch to 'mydatabase'
db.createUser({
  user: "myuser",
  pwd: "mypassword",
  roles: [
    {
      role: "readWrite",
      db: "mydatabase"
    }
  ]
});
db.mycollection.insertMany([
  { name: "John Doe", age: 30, occupation: "Engineer" },
  { name: "Jane Doe", age: 25, occupation: "Doctor" }
]);
