<script>
    import Bargraph from "../components/charts/bargraph.svelte";
    import Gauge from "../components/charts/gauge.svelte";
    import Linegraph from "../components/charts/linegraph.svelte";

</script>


<main class="grid">
    <h1>Analysis</h1>
    <h2>Distributions</h2>
    <p>Vivamus non dolor tellus. Cras tincidunt magna vitae diam imperdiet aliquet. Morbi euismod aliquam tincidunt. Sed est urna, scelerisque et fringilla id, scelerisque id sapien. Ut in pulvinar elit. Curabitur vitae risus non elit rhoncus vulputate. Pellentesque non ligula vel leo imperdiet rutrum vel vel neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed tempus dignissim consequat. Maecenas mi nulla, vestibulum consequat leo non, ornare convallis diam. Ut sapien ipsum, maximus sit amet ornare ut, condimentum id lacus. Pellentesque nec sapien in urna fringilla laoreet. Praesent interdum lacus ac pharetra pulvinar. Sed fringilla id lorem eget euismod. Nulla et eros libero.</p>
    <img src="static\hist_fat.png" alt="">
    <h2>Correlations</h2>
    <p>Vivamus non dolor tellus. Cras tincidunt magna vitae diam imperdiet aliquet. Morbi euismod aliquam tincidunt. Sed est urna, scelerisque et fringilla id, scelerisque id sapien. Ut in pulvinar elit. Curabitur vitae risus non elit rhoncus vulputate. Pellentesque non ligula vel leo imperdiet rutrum vel vel neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed tempus dignissim consequat. Maecenas mi nulla, vestibulum consequat leo non, ornare convallis diam. Ut sapien ipsum, maximus sit amet ornare ut, condimentum id lacus. Pellentesque nec sapien in urna fringilla laoreet. Praesent interdum lacus ac pharetra pulvinar. Sed fringilla id lorem eget euismod. Nulla et eros libero.</p>
    <img src="static\cross-correlation.png" alt="">
    <h3>Causations</h3>
    <h4>Light Intensity, EC and pH</h4>
    <p></p>
    <img src="" alt="">
    <h4>Is your heating any good?</h4>
    <p></p>
    <img src="" alt="">
    <h2>Auto-Correlation</h2>
    <p>Vivamus non dolor tellus. Cras tincidunt magna vitae diam imperdiet aliquet. Morbi euismod aliquam tincidunt. Sed est urna, scelerisque et fringilla id, scelerisque id sapien. Ut in pulvinar elit. Curabitur vitae risus non elit rhoncus vulputate. Pellentesque non ligula vel leo imperdiet rutrum vel vel neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed tempus dignissim consequat. Maecenas mi nulla, vestibulum consequat leo non, ornare convallis diam. Ut sapien ipsum, maximus sit amet ornare ut, condimentum id lacus. Pellentesque nec sapien in urna fringilla laoreet. Praesent interdum lacus ac pharetra pulvinar. Sed fringilla id lorem eget euismod. Nulla et eros libero.</p>
    <img src="static\autocorrelation.png" alt="">



</main>


<style>

    p {
        grid-column: content-start / span 6;
    }

    img {
        grid-column: span 6;
        max-width: 100%;
    }

</style>