<script>
    let health;

    fetch("http://127.0.0.1:8000/health").then((response) => {
        response.json().then((json) => {
            health = json;
        });
    });
</script>

{#if health}
    <div>
        <h1>Status: {health.status}</h1>
        <p>Version: {health.version}</p>
        <p>Timestamp: {health.timestamp}</p>
    </div>
{:else}
    <p>Loading...</p>
{/if}