<script>
	import { onMount } from 'svelte';

	let chart;
    export let data = [65, 59, 80, 81, 56, 55, 40]
    export let label = "Dataset"
    export let borderWidth = 3
    export let datasets = [
        {
            label,
            data,
            borderWidth,
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgba(255, 99, 132, 0.2)"
        },
        // {
        //     label: "My Second Dataset",
        //     data: [10,10,20,30,50,70,120,190],
        //     borderWidth: 3,
        //     backgroundColor: "rgba(255, 99, 255, 0.2)",
        //     borderColor: "rgba(255, 99, 255, 0.2)"
        // }
    ]

    export let labels = [];
    export let beginZero = true;
    export let style =  "grid-column: content-start / content-end; width: 100%;"

    console.log(data)

    const data_combined = {
        labels,
        datasets
    };
    
    const config = {
        type: 'line',
        data: data_combined,
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