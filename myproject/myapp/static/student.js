// Student registration form functionality

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('studentForm');
    const successMessage = document.getElementById('successMessage');
    
    // Course fee mapping
    const courseFees = {
        'data-analysis': 1800,
        'web-development': 2500,
        'graphics-design': 1500,
        'digital-marketing': 1200,
        'content-creation': 1000
    };
    
    // Auto-populate enrollment fee based on selected course
    const courseSelect = document.getElementById('courseInterest');
    const feeInput = document.getElementById('enrollmentFee');
    
    courseSelect.addEventListener('change', function() {
        const selectedCourse = this.value;
        if (selectedCourse && courseFees[selectedCourse]) {
            feeInput.value = courseFees[selectedCourse];
        }
    });
    
    // Form submission handler
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (validateForm()) {
            submitForm();
        }
    });
    
    // Real-time validation
    const inputs = form.querySelectorAll('input, select');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateField(this);
        });
        
        input.addEventListener('input', function() {
            clearError(this);
        });
    });
});

function validateForm() {
    const studentName = document.getElementById('studentName');
    const courseInterest = document.getElementById('courseInterest');
    const courseDuration = document.getElementById('courseDuration');
    const enrollmentFee = document.getElementById('enrollmentFee');
    
    let isValid = true;
    
    // Validate student name
    if (!validateField(studentName)) {
        isValid = false;
    }
    
    // Validate course selection
    if (!validateField(courseInterest)) {
        isValid = false;
    }
    
    // Validate duration
    if (!validateField(courseDuration)) {
        isValid = false;
    }
    
    // Validate enrollment fee
    if (!validateField(enrollmentFee)) {
        isValid = false;
    }
    
    return isValid;
}

function validateField(field) {
    const fieldName = field.name;
    const value = field.value.trim();
    let isValid = true;
    let errorMessage = '';
    
    // Clear previous errors
    clearError(field);
    
    switch(fieldName) {
        case 'studentName':
            if (!value) {
                errorMessage = 'Student name is required';
                isValid = false;
            } else if (value.length < 2) {
                errorMessage = 'Name must be at least 2 characters long';
                isValid = false;
            } else if (!/^[a-zA-Z\s]+$/.test(value)) {
                errorMessage = 'Name can only contain letters and spaces';
                isValid = false;
            }
            break;
            
        case 'courseInterest':
            if (!value) {
                errorMessage = 'Please select a course';
                isValid = false;
            }
            break;
            
        case 'courseDuration':
            if (!value) {
                errorMessage = 'Please select course duration';
                isValid = false;
            }
            break;
            
        case 'enrollmentFee':
            if (!value) {
                errorMessage = 'Enrollment fee is required';
                isValid = false;
            } else if (isNaN(value) || parseFloat(value) <= 0) {
                errorMessage = 'Please enter a valid fee amount';
                isValid = false;
            } else if (parseFloat(value) > 10000) {
                errorMessage = 'Fee amount seems too high. Please verify.';
                isValid = false;
            }
            break;
    }
    
    if (!isValid) {
        showError(field, errorMessage);
    }
    
    return isValid;
}

function showError(field, message) {
    const errorElement = document.getElementById(field.name.replace(/([A-Z])/g, '') + 'Error');
    if (errorElement) {
        errorElement.textContent = message;
        errorElement.classList.add('show');
    }
    
    field.style.borderColor = '#e74c3c';
}

function clearError(field) {
    const errorElement = document.getElementById(field.name.replace(/([A-Z])/g, '') + 'Error');
    if (errorElement) {
        errorElement.textContent = '';
        errorElement.classList.remove('show');
    }
    
    field.style.borderColor = '';
}

function submitForm() {
    const form = document.getElementById('studentForm');
    const submitBtn = form.querySelector('.register-btn');
    const successMessage = document.getElementById('successMessage');
    
    // Disable submit button
    submitBtn.disabled = true;
    submitBtn.textContent = 'Registering...';
    
    // Simulate form submission
    setTimeout(() => {
        // Hide form and show success message
        form.style.display = 'none';
        successMessage.style.display = 'block';
        
        // Show notification
        utils.showNotification('Student registered successfully!', 'success');
        
        // Reset form after delay
        setTimeout(() => {
            resetForm();
        }, 3000);
        
    }, 2000);
}

function resetForm() {
    const form = document.getElementById('studentForm');
    const successMessage = document.getElementById('successMessage');
    const submitBtn = form.querySelector('.register-btn');
    
    // Reset form
    form.reset();
    form.style.display = 'block';
    successMessage.style.display = 'none';
    
    // Re-enable submit button
    submitBtn.disabled = false;
    submitBtn.textContent = 'Register Student';
    
    // Clear any remaining errors
    const errorMessages = form.querySelectorAll('.error-message');
    errorMessages.forEach(error => {
        error.textContent = '';
        error.classList.remove('show');
    });
    
    // Reset input styles
    const inputs = form.querySelectorAll('input, select');
    inputs.forEach(input => {
        input.style.borderColor = '';
    });
}