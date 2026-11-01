// Selected original LZ helpers. Function definitions below are unchanged.
// This file contains only two excerpts; it is not the complete memory engine.

function localOnlyRecord(record) {
  // A rendered containing record can include nested JSON fields. Privacy on
  // any such descendant taints the containing document; child `false` never
  // overrides a parent boundary. Malformed present flags fail closed.
  const pending = [record];
  let inspected = 0;
  while (pending.length) {
    if (++inspected > 100000) return true;
    const value = pending.pop();
    if (!value || typeof value !== 'object') continue;
    for (const key of ['localMemoryOnly', 'local_memory_only']) if (Object.hasOwn(value, key) && value[key] !== false) return true;
    for (const child of Object.values(value)) if (child && typeof child === 'object') pending.push(child);
  }
  return false;
}

function excerptFor(document, words, maxChars) {
  const text = document.text, normalized = document.normalized;
  let bestStart = 0, bestScore = -1;
  for (const word of words) {
    let position = normalized.indexOf(word), visits = 0;
    while (position !== -1 && visits++ < 80) {
      const start = Math.max(0, position - Math.floor(maxChars / 4));
      const window = normalized.slice(start, start + maxChars);
      const score = words.reduce((sum, token) => sum + (window.includes(token) ? 1 : 0), 0);
      if (score > bestScore) { bestScore = score; bestStart = start; }
      position = normalized.indexOf(word, position + word.length);
    }
  }
  const excerpt = text.slice(bestStart, bestStart + maxChars);
  return `${bestStart ? '[excerpt] ' : ''}${excerpt}${bestStart + maxChars < text.length ? '\n[excerpt continues]' : ''}`;
}

export { localOnlyRecord, excerptFor };
