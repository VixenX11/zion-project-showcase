// Newly written teaching demo inspired by version checks in Secretary Zion.
// This is not the original service. It has no persistence or external actions.
import { pathToFileURL } from 'node:url';

export function updateTask(task, expectedVersion, changes) {
  if (!task || typeof task.id !== 'string' || !task.id.trim()) {
    throw new TypeError('A task with a nonempty string id is required.');
  }
  if (!Number.isSafeInteger(task.version) || task.version < 0) {
    throw new TypeError('Task version must be a nonnegative safe integer.');
  }
  if (!Number.isSafeInteger(expectedVersion)) {
    throw new TypeError('Expected version must be a safe integer.');
  }
  if (expectedVersion !== task.version) {
    throw new Error(`Version conflict: expected ${expectedVersion}, current ${task.version}.`);
  }
  if (task.version === Number.MAX_SAFE_INTEGER) {
    throw new RangeError('Task version cannot be incremented safely.');
  }
  if (!changes || typeof changes !== 'object' || Array.isArray(changes)) {
    throw new TypeError('Changes must be an object.');
  }
  if (Object.keys(changes).some(key => !['title', 'status'].includes(key))) {
    throw new TypeError('Only title and status can be changed in this demo.');
  }
  if ('title' in changes && (typeof changes.title !== 'string' || !changes.title.trim())) {
    throw new TypeError('Title must be a nonempty string.');
  }
  if ('status' in changes && !['todo', 'doing', 'done'].includes(changes.status)) {
    throw new TypeError('Status must be todo, doing, or done.');
  }
  const updated = { ...task, ...changes, version: task.version + 1 };
  const receipt = {
    scope: 'in-memory-demo',
    taskId: task.id,
    previousVersion: task.version,
    version: updated.version,
  };
  return { task: updated, receipt };
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const original = { id: 'demo-task', title: 'Prepare a sample briefing', status: 'todo', version: 1 };
  const result = updateTask(original, 1, { status: 'doing' });
  console.log(JSON.stringify({ original, ...result }, null, 2));
  try {
    updateTask(result.task, 1, { status: 'done' });
  } catch (error) {
    console.log(`Stale update rejected: ${error.message}`);
  }
}
