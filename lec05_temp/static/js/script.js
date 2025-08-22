// ملف JavaScript لنظام إدارة الطلاب

document.addEventListener('DOMContentLoaded', function() {

    // تأثيرات بصرية للجداول
    const tables = document.querySelectorAll('.table');
    tables.forEach(table => {
        const rows = table.querySelectorAll('tbody tr');
        rows.forEach((row, index) => {
            row.style.animationDelay = `${index * 0.1}s`;
            row.classList.add('fade-in-row');
        });
    });

    // تأثيرات للكروت
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.2}s`;
        card.classList.add('fade-in-card');
    });

    // تحسين تفاعل الأزرار
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            // تأثير الضغط
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    });

    // تأكيد الحذف (إذا كان هناك أزرار حذف في المستقبل)
    const deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('هل أنت متأكد من هذا الإجراء؟')) {
                e.preventDefault();
            }
        });
    });

    // تحسين البحث (للاستخدام المستقبلي)
    const searchInputs = document.querySelectorAll('input[type="search"]');
    searchInputs.forEach(input => {
        input.addEventListener('input', function() {
            // يمكن إضافة وظائف البحث الفوري هنا
            console.log('البحث عن:', this.value);
        });
    });

    // إضافة تلميحات للأزرار
    const tooltipElements = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    if (tooltipElements.length > 0 && typeof bootstrap !== 'undefined') {
        tooltipElements.forEach(element => {
            new bootstrap.Tooltip(element);
        });
    }

    // تحسين النماذج
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitButton = form.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>جاري التحميل...';
                submitButton.disabled = true;
            }
        });
    });

    console.log('✅ تم تحميل نظام إدارة الطلاب بنجاح');
});

// دالة لإظهار رسائل التنبيه
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    const container = document.querySelector('main .container');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);

        // إزالة التنبيه تلقائياً بعد 5 ثوان
        setTimeout(() => {
            if (alertDiv && alertDiv.parentNode) {
                alertDiv.remove();
            }
        }, 5000);
    }
}

// دالة لطباعة الجدول
function printTable() {
    window.print();
}

// إضافة الأنماط المتحركة
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeInRow {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInCard {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .fade-in-row {
        animation: fadeInRow 0.6s ease forwards;
        opacity: 0;
    }

    .fade-in-card {
        animation: fadeInCard 0.8s ease forwards;
        opacity: 0;
    }
`;
document.head.appendChild(style);