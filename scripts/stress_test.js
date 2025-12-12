import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '20s', target: 50 },
    { duration: '30s', target: 150 },
    { duration: '20s', target: 300 },
    { duration: '20s', target: 0 },
  ],
};

export default function () {
  let res = http.get('https://www.saucedemo.com/');
  check(res, { 'status was 200': (r) => r.status === 200 });
  sleep(1);
}

