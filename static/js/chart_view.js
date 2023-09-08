async function chartLoadData() {
    try {
        const response = await fetch('/chart_load/');
        const cryptos_market_chart = await response.json();
        return cryptos_market_chart;
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

async function chartBuild(chartElement) {
    try {
        const data = await chartLoadData();
        console.log(data.prices)
        const dates = data.dates
        let cryptosData = []
        for (const crypto in data.prices) {
            cryptosData.push({
                label: crypto,
                data: data.prices[crypto]
            })
        }
        new Chart(chartElement,
            {
                type: 'line',
                data: {
                    labels: dates,
                    datasets: cryptosData
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

    } catch (error) {
        // Handle errors here if needed
    }
}

function initializeChartLoader() {
    const chartElement = document.getElementById('cryptoChart');
    if (chartElement) {
        chartBuild(chartElement);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    initializeChartLoader();
});