// Revenue Activities Per Month (Bar)
function initializeStudentsChart() {
    const ctx = document.getElementById("studentsChart");
    if (!ctx) return;

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
            ],
            datasets: [{
                label: "Revenue (₦)",
                data: window.revenueData,   // monthly revenue
                backgroundColor: [
                    '#9bbbfc', '#f9ce69', '#4741a6',
                    '#d9eff7', '#ff9a9e', '#88d498',
                    '#ff6f61', '#6a0572', '#00bcd4',
                    '#ffc107', '#4caf50', '#e91e63'
                ],
                borderRadius: 6,
                barPercentage: 0.5,
                categoryPercentage: 0.6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            layout: {
                padding: { top: 10, bottom: 10, left: 10, right: 10 }
            },
            plugins: { legend: { display: false } },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: (value) => '₦' + value.toLocaleString()
                    }
                }
            }
        }
    });
}

// Revenue Trend (Line)
function initializeRevenueChart() {
    const ctx = document.getElementById("revenueChart");
    if (!ctx) return;

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: [
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
            ],
            datasets: [{
                label: 'Monthly Revenue',
                data: window.revenueData,   // same monthly revenue
                borderColor: '#4741a6',
                backgroundColor: 'rgba(71, 65, 166, 0.1)',
                tension: 0.4,
                fill: true,
                pointBackgroundColor: '#4741a6',
                pointBorderColor: '#ffffff',
                pointBorderWidth: 2,
                pointRadius: 5
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            layout: {
                padding: { top: 10, bottom: 10, left: 10, right: 10 }
            },
            plugins: { legend: { display: false } },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: (value) => '₦' + value.toLocaleString()
                    }
                }
            }
        }
    });
}


// Initialize charts when page loads
document.addEventListener("DOMContentLoaded", function () {
    initializeStudentsChart();
    initializeRevenueChart();
});
