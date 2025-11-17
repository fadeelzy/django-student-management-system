// Revenue page JavaScript functionality  
document.addEventListener('DOMContentLoaded', function() {
    initializeCourseRevenueChart();
    initializeMonthlyRevenueChart();
    setTimeout(animateRevenueSummary, 800);
});

// ✅ Use Django-passed data
const revenueData = window.revenueData || { courses: {}, monthly: {} }
function initializeCourseRevenueChart() {
    const ctx = document.getElementById('courseRevenueChart');
    if (!ctx) return;

    const labels = Object.keys(revenueData.courses);
    const values = Object.values(revenueData.courses);

    new Chart(ctx, {
        type: 'bar',   
        data: {
            labels: labels,
            datasets: [{
                label: 'Revenue by Course (₦)',   
                data: values,
                backgroundColor: [
                    '#4741a6',
                    '#9bbbfc',
                    '#f9ce69',
                    '#d9eff7',
                    '#6c757d'
                ],
                borderWidth: 1,
                borderColor: '#333'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Courses'
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Revenue (₦)'
                    },
                    ticks: {
                        callback: function(value) {
                            return '₦' + value.toLocaleString();
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: false 
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const value = context.parsed.y;
                            return `₦${value.toLocaleString()}`;
                        }
                    }
                }
            }
        }
    });
}

// --- Monthly Revenue Chart ---
function initializeMonthlyRevenueChart() { 
    const ctx = document.getElementById('monthlyRevenueChart');
    if (!ctx) return;

    const labels = Object.keys(revenueData.monthly);
    const values = Object.values(revenueData.monthly);

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: "Members Monthly Revenue",
                data: values,
                borderColor: '#4741a6',
                backgroundColor: 'rgba(71, 65, 166, 0.1)',
                tension: 0.4,          // smooth curve
                fill: true,
                borderWidth: 2,
                pointBackgroundColor: '#4741a6',
                pointRadius: 4,
                spanGaps: true         //  connect missing months instead of breaking the line
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: 'index',
                intersect: false,
            },
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Month'
                    }
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Revenue (₦)'
                    },
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return '₦' + value.toLocaleString();
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 15,
                        font: {
                            size: 11
                        }
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return "₦" + context.parsed.y.toLocaleString();
                        }
                    }
                }
            }
        }
    });
}

// --- Animate summary numbers ---
function animateRevenueSummary() {
    const revenueAmounts = document.querySelectorAll('.revenue-amount');
    
    revenueAmounts.forEach(amount => {
        const finalValue = parseFloat(amount.dataset.value);
        if (isNaN(finalValue)) return;
        
        let currentValue = 0;
        const increment = Math.ceil(finalValue / 60);
        
        const updateValue = () => {
            currentValue += increment;
            if (currentValue >= finalValue) {
                currentValue = finalValue;
                clearInterval(counter);
            }
            amount.textContent = '₦' + currentValue.toLocaleString();
        };
        
        const counter = setInterval(updateValue, 25);
    });
}
