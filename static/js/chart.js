document.addEventListener("DOMContentLoaded", function () {
            // Get the canvas element
            var ctx = document.getElementById("cryptoChart").getContext("2d");

            // Create a line chart with string labels for the x-axis
            var myChart = new Chart(ctx, {
                type: "line",
                data: {
                    labels: [1], // String labels for x-axis
                    datasets: [
                            {
                                label: '',
                                data: [1], // Corresponding data for y-axis
                                borderColor: "rgba(75, 192, 192, 1)",
                                backgroundColor: "rgba(75, 192, 192, 1)",
                                borderWidth: 2,
                                fill: false,
                            },

                    ],
                },
                options: {
                    responsive: true, // Allow the chart to be responsive
                    scales: {
                        x: {
                            type: "category", // Specify that x-axis contains category data
                            position: "bottom",
                        },
                        y: {
                            beginAtZero: true, // Start the y-axis at zero
                        },
                    },
                },
            });
        });