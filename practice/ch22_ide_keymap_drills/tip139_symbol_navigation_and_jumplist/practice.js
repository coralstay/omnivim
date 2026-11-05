async function fetchUserById(id) {
  return db.users.find(id);
}
const user = await legacyFetchUser(42);
