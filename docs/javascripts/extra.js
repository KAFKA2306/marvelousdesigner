// VRChat衣装制作ガイド - 追加JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // 進捗チェックリストの機能
    initProgressCheckboxes();
    
    // ページ内検索の改善
    improveSearch();
    
    // 外部リンクに新しいタブで開く属性を追加
    addTargetBlankToExternalLinks();
});

// 進捗チェックボックスの状態をローカルストレージに保存
function initProgressCheckboxes() {
    const checkboxes = document.querySelectorAll('.progress-checklist input[type="checkbox"]');
    
    checkboxes.forEach(function(checkbox, index) {
        const pageUrl = window.location.pathname;
        const checkboxId = `${pageUrl}_checkbox_${index}`;
        
        // 保存された状態を読み込み
        const savedState = localStorage.getItem(checkboxId);
        if (savedState === 'true') {
            checkbox.checked = true;
        }
        
        // チェック状態の変更を保存
        checkbox.addEventListener('change', function() {
            localStorage.setItem(checkboxId, checkbox.checked);
        });
    });
}

// 検索機能の改善（日本語検索対応）
function improveSearch() {
    const searchInput = document.querySelector('[data-md-component="search-query"]');
    if (searchInput) {
        searchInput.setAttribute('placeholder', 'ガイドを検索...');
    }
}

// 外部リンクを新しいタブで開く
function addTargetBlankToExternalLinks() {
    const links = document.querySelectorAll('a[href^="http"]:not([href*="' + window.location.hostname + '"])');
    links.forEach(function(link) {
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
    });
}

// ソフトウェアバージョン情報の更新日時を表示
function updateVersionInfo() {
    const versionElements = document.querySelectorAll('.software-version');
    const lastUpdated = new Date().toLocaleDateString('ja-JP');
    
    versionElements.forEach(function(element) {
        element.setAttribute('title', `最終更新: ${lastUpdated}`);
    });
}

// ステップガイドのナビゲーション改善
function enhanceStepNavigation() {
    const steps = document.querySelectorAll('.step-container');
    steps.forEach(function(step, index) {
        step.setAttribute('id', `step-${index + 1}`);
    });
}

// ページ読み込み完了時の追加処理
window.addEventListener('load', function() {
    updateVersionInfo();
    enhanceStepNavigation();
});