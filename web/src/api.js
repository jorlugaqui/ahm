const { VUE_APP_API_HOST } = process.env;

function fetchReport(period) {
  const path = `${VUE_APP_API_HOST}/v1/report/${period}`;
  return fetch(path)
    .then((res) => res.json());
}


export default {
  fetchReport,
};
