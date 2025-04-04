// ==UserScript==
// @name         AniList to Nyaa Search (In-Page) with URL Extracted Title
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Open a mini window inside AniList with the Nyaa search results for the anime title and an easy way to close it.
// @author       You
// @match        https://anilist.co/anime/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Function to extract the anime title from the page content
    function getAnimeTitleFromPage() {
        // Try to get the title from the h1 element
        const titleElement = document.querySelector('h1[data-v-5776f768]');

        if (titleElement) {
            // Return the content of the h1 element
            return titleElement.textContent.trim();
        }

        // Fallback: if title is not in the h1 tag, try extracting from URL
        const pathSegments = window.location.pathname.split('/');
        const animeTitleFromUrl = pathSegments[pathSegments.length - 1];

        return animeTitleFromUrl ? decodeURIComponent(animeTitleFromUrl) : null;
    }

    // Function to create and open a mini window for Nyaa search
    function openNyaaMiniWindow(animeTitle) {
        const searchURL = `https://nyaa.si/?f=0&c=0_0&q=${encodeURIComponent(animeTitle)}`;

        // Create a small iframe to embed Nyaa search in the page
        const iframe = document.createElement('iframe');
        iframe.src = searchURL;
        iframe.style.position = 'fixed';
        iframe.style.top = '0';
        iframe.style.right = '0';
        iframe.style.width = '600px';
        iframe.style.height = '400px';
        iframe.style.border = 'none';
        iframe.style.zIndex = '1000';
        iframe.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.3)';
        iframe.style.borderRadius = '8px';

        // Append the iframe to the body
        document.body.appendChild(iframe);

        // Add a close button to remove the iframe when clicked
        const closeButton = document.createElement('button');
        closeButton.innerText = 'X';  // Simple close button text
        closeButton.style.position = 'absolute';
        closeButton.style.top = '5px';
        closeButton.style.right = '5px';
        closeButton.style.padding = '5px 10px';
        closeButton.style.backgroundColor = '#ff4081';
        closeButton.style.color = 'white';
        closeButton.style.border = 'none';
        closeButton.style.borderRadius = '50%';
        closeButton.style.cursor = 'pointer';
        closeButton.style.fontSize = '14px';
        closeButton.style.zIndex = '1001';

        closeButton.addEventListener('click', function() {
            document.body.removeChild(iframe);
            document.body.removeChild(closeButton);
        });

        // Append the close button to the iframe container
        iframe.contentWindow.document.body.appendChild(closeButton);
    }

    // Create the button to trigger the mini window
    function createButton() {
        const button = document.createElement('button');
        button.innerText = 'Open Nyaa Torrent Search';
        button.style.position = 'fixed';
        button.style.bottom = '20px';
        button.style.right = '20px';
        button.style.padding = '10px 20px';
        button.style.fontSize = '16px';
        button.style.backgroundColor = '#ff4081';
        button.style.color = 'white';
        button.style.border = 'none';
        button.style.borderRadius = '5px';
        button.style.cursor = 'pointer';
        button.style.zIndex = '1000';
        button.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.3)';

        button.addEventListener('click', function() {
            const animeTitle = getAnimeTitleFromPage();
            if (animeTitle) {
                openNyaaMiniWindow(animeTitle);
            } else {
                alert('Could not retrieve anime title from the page.');
            }
        });

        // Append the button to the page
        document.body.appendChild(button);
    }

    // Wait until the page is loaded
    window.addEventListener('load', createButton);
})();
