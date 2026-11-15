import express from 'express';
import path from 'node:path';
import { readFileSync } from 'node:fs';

export const app = express();
app.disable('x-powered-by');
app.use(express.static(path.join(process.cwd(), 'public')));
app.get('/api/health', (_req, res) => {
  let build = process.env.BUILD_SOURCEVERSION || 'local';
  try { build = readFileSync(path.join(process.cwd(), 'build-sha.txt'), 'utf8').trim() || build; } catch { /* Local run has no build artifact. */ }
  res.json({status:'ok', app:'PulseOps', version:process.env.APP_VERSION || '2', build});
});
