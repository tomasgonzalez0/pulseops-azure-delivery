const { test } = require('node:test');
const assert = require('node:assert/strict');
const { app } = require('../dist/app');

test('health endpoint reports deployment identity', async () => {
  const server = app.listen(0);
  try {
    const response = await fetch(`http://127.0.0.1:${server.address().port}/api/health`);
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.equal(body.status, 'ok');
    assert.equal(body.app, 'PulseOps');
    assert.ok(body.version);
    assert.ok(body.build);
  } finally { server.close(); }
});
