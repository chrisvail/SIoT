<script>
	import { onMount } from 'svelte';

	let chart;

    export let datasets = [{
            label: 'My First Dataset',
            data: [65, 59, 80, 81, 56, 55, 40],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)'
            ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
            ],
            borderWidth: 1
        }]

    export let labels = "a b c d e f g".split(" ");
    export let beginZero = true;
    export let style =  "grid-column: content-start / content-end; width: 100%;"

    const data = {
        labels,
        datasets
    };
    
    const config = {
        type: 'bar',
        data: data,
        options: {
            scales: {
            y: {
                beginAtZero: beginZero
            }
            }
        },
    };

    onMount(() => {
        let barChart = new Chart(chart, config)
    })

</script>

<div class="chart-wrap" {style}>
    <canvas bind:this={chart} id="myChart"></canvas>
</div>


<style>


</style>