const { VUE_APP_API_HOST } = process.env;

function fetchReport(period) {
  const path = `${VUE_APP_API_HOST}/v1/report/${period}`;
  return fetch(path);
}

function sendMeasurement(measurement) {
  const path = `${VUE_APP_API_HOST}/v1/measurements`;
  return fetch(path, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(measurement),
  });
}

function getMeasurement(id) {
  const path = `${VUE_APP_API_HOST}/v1/measurements/${id}`;
  return fetch(path);
}

function updateMeasurement(measurement) {
  const path = `${VUE_APP_API_HOST}/v1/measurements/${measurement.id}`;
  return fetch(path, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(measurement),
  });
}

/**
 * Based on https://gist.github.com/odewahn/5a5eeb23279eed6a80d7798fdb47fe91
 */
function parseJSON(response) {
  return new Promise((resolve) => response.json()
    .then((json) => resolve({
      status: response.status,
      ok: response.ok,
      json,
    })));
}


export default {
  fetchReport,
  sendMeasurement,
  getMeasurement,
  updateMeasurement,
  parseJSON,
};
