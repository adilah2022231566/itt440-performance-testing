import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 10,
  duration: '10m', // you can reduce to 5m if needed
};

export default function () {
  let res = http.get('https://www.saucedemo.com/');
  check(res, { 'status was 200': (r) => r.status === 200 });
  sleep(1);
}
