<script>
    import { onMount } from "svelte";
	
	let headerText;

    export let style

    let chart;
    export let comment = "This is a little comment about whats happening up there"
    export let title = "EC"
    export let value = 200
    export let reference = 160
    export let range = [20, 320]
    export let data = [
    {
        type: "indicator",
        value,
        delta: { reference },
        gauge: { axis: { visible: false, range} },
        domain: { row: 0, column: 0 }
    },
    // {
    //     type: "indicator",
    //     value: 120,
    //     gauge: {
    //     shape: "bullet",
    //     axis: {
    //         visible: false,
    //         range: [-200, 200]
    //     }
    //     },
    //     domain: { x: [0.1, 0.5], y: [0.15, 0.35] }
    // },
    // {
    //     type: "indicator",
    //     mode: "number+delta",
    //     value: 300,
    //     domain: { row: 0, column: 1 }
    // },
    // { type: "indicator", mode: "delta", value: 40, domain: { row: 1, column: 1 } }
    ];

    export let layout = {
    width: 300,
    height: 200,
    margin: { t: 25, b: 25, l: 25, r: 25 },
    grid: { rows: 1, columns: 1, pattern: "independent" },
    template: {
        data: {
        indicator: [
            {
            title: { text: title },
            mode: "number+gauge",
            delta: { reference: 90 }
            }
        ]
        }
    }
    };

    onMount(() => {
            headerText = 'On Mount Called !';
            // let plotDiv = document.getElementById('plotDiv');				
            let Plot = new Plotly.newPlot(chart, data, layout, {showSendToCloud:true}); 
    });

</script>

<div class="wrapper" {style}>
    <div bind:this={chart} class="container">
    <p>{comment}</p>
</div>

</div>


<style>

    p {
        max-width: 300px;
        text-align: center;
        color: var(--txt-mid);
        font-style: italic;
        font-size: 1em;
    }

</style>