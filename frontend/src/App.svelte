<script>
  let health;
  let error = null;

  fetch("http://127.0.0.1:8000/health")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Health check failed with status ${response.status}`);
      }
      return response.json();
    })
    .then((json) => {
      health = json;
    })
    .catch((err) => {
      console.error("Failed to fetch health check: ", err);
      error = "Failed to load service status";
    });
</script>

{#if error}
  <h1>Error</h1>
  <p>{error}</p>
{:else if health}
  <div>
    <h1>Status: {health.status}</h1>
    <p>Version: {health.version}</p>
    <p>Timestamp: {health.timestamp}</p>
  </div>
{:else}
  <p>Loading...</p>
{/if}
