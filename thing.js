// ==UserScript==
// @name         AniList to Nyaa Search (Title Toggle with Nyaa Search)
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Toggle between English, Romanji, and Native titles and show Nyaa search iframe under episodes on AniList.
// @author       You
// @match        https://anilist.co/anime/*
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    console.log('Script is running...');

    // Helper: Get anime title from different sources
    function getAnimeTitles() {
        const titleElement = document.querySelector('h1[data-v-5776f768]');
        console.log('Title Element:', titleElement);
        const data = titleElement ? titleElement.closest('[data-v-d3a518a6]') : null;
        console.log('Data:', data);
        if (data) {
            return {
                english: data.dataset.english || '',
                romanji: data.dataset.romanji || '',
                native: data.dataset.native || '',
            };
        }
        return { english: '', romanji: '', native: '' };
    }

    // Helper: Create the Nyaa search iframe
    function openNyaaMiniWindow(animeTitle) {
        console.log('Opening Nyaa iframe for title:', animeTitle);
        const searchURL = `https://nyaa.si/?f=0&c=0_0&q=${encodeURIComponent(animeTitle)}`;

        const iframe = document.createElement('iframe');
        iframe.src = searchURL;
        iframe.style.display = 'none';  // Initially hidden
        iframe.style.width = '100%';
        iframe.style.height = '400px';
        iframe.style.border = 'none';
        iframe.style.marginTop = '1em';
        iframe.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.3)';
        iframe.style.borderRadius = '8px';

        document.body.appendChild(iframe);

        return iframe;
    }

    // Helper: Create the title toggle buttons
    function injectTitleToggle(titles, animeTitle) {
        const sidebar = document.querySelector('.content .sidebar, .media-sidebar');
        if (!sidebar || document.querySelector('#title-toggle-wrapper')) {
            console.log('Sidebar not found or already injected');
            return;
        }

        console.log('Sidebar found:', sidebar);

        const wrapper = document.createElement('div');
        wrapper.id = 'title-toggle-wrapper';
        wrapper.style.marginTop = '1.5em';
        wrapper.style.textAlign = 'center';

        const button = document.createElement('button');
        button.textContent = 'Show Title Options';
        button.style.backgroundColor = '#2b2d42';
        button.style.color = '#fff';
        button.style.padding = '10px 20px';
        button.style.border = 'none';
        button.style.borderRadius = '5px';
        button.style.cursor = 'pointer';
        button.style.fontSize = '14px';

        const englishButton = document.createElement('button');
        englishButton.textContent = `English: ${titles.english}`;
        englishButton.style.margin = '5px';
        englishButton.style.backgroundColor = '#1f4068';
        englishButton.style.color = '#fff';
        englishButton.style.padding = '8px 15px';
        englishButton.style.border = 'none';
        englishButton.style.borderRadius = '5px';
        englishButton.style.fontSize = '12px';

        const romanjiButton = document.createElement('button');
        romanjiButton.textContent = `Romanji: ${titles.romanji}`;
        romanjiButton.style.margin = '5px';
        romanjiButton.style.backgroundColor = '#1f4068';
        romanjiButton.style.color = '#fff';
        romanjiButton.style.padding = '8px 15px';
        romanjiButton.style.border = 'none';
        romanjiButton.style.borderRadius = '5px';
        romanjiButton.style.fontSize = '12px';

        const nativeButton = document.createElement('button');
        nativeButton.textContent = `Native: ${titles.native}`;
        nativeButton.style.margin = '5px';
        nativeButton.style.backgroundColor = '#1f4068';
        nativeButton.style.color = '#fff';
        nativeButton.style.padding = '8px 15px';
        nativeButton.style.border = 'none';
        nativeButton.style.borderRadius = '5px';
        nativeButton.style.fontSize = '12px';

        const nyaaIframe = openNyaaMiniWindow(animeTitle);

        let iframeVisible = false;
        button.addEventListener('click', () => {
            iframeVisible = !iframeVisible;
            nyaaIframe.style.display = iframeVisible ? 'block' : 'none';
            button.textContent = iframeVisible ? 'Hide Title Options' : 'Show Title Options';

            const isVisible = englishButton.style.display === 'block';
            englishButton.style.display = isVisible ? 'none' : 'block';
            romanjiButton.style.display = isVisible ? 'none' : 'block';
            nativeButton.style.display = isVisible ? 'none' : 'block';
        });

        wrapper.appendChild(button);
        wrapper.appendChild(englishButton);
        wrapper.appendChild(romanjiButton);
        wrapper.appendChild(nativeButton);
        sidebar.appendChild(wrapper);
    }

    // Retry mechanism to ensure the data is available and the page has fully loaded
    function waitForTitles(retryCount = 0) {
        if (retryCount > 5) {
            console.log('Max retries reached, stopping...');
            return;
        }

        const titles = getAnimeTitles();
        if (!titles.english && !titles.romanji && !titles.native) {
            console.log('Titles not found, retrying...');
            setTimeout(() => waitForTitles(retryCount + 1), 1000); // Retry every second
        } else {
            const animeTitle = titles.english || titles.romanji || titles.native;
            console.log('Titles found:', titles);
            injectTitleToggle(titles, animeTitle);
        }
    }

    // Start the retry mechanism after page load
    window.addEventListener('load', () => {
        console.log('Page loaded, starting title check...');
        waitForTitles();
    });

})();
