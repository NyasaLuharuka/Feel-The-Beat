const entryInput = document.getElementById('entry');
const saveBtn = document.getElementById('save');
const entriesList = document.getElementById('entriesList');

document.addEventListener('DOMContentLoaded', loadEntries);

saveBtn.addEventListener('click', () => {
  const entryText = entryInput.value.trim();
  if (entryText === '') return alert('Please write something before saving.');

  const entries = JSON.parse(localStorage.getItem('journalEntries')) || [];
  const timestamp = new Date().toLocaleString();

  entries.push({ text: entryText, date: timestamp });
  localStorage.setItem('journalEntries', JSON.stringify(entries));

  entryInput.value = '';
  loadEntries();
});

// Load entries from localStorage
function loadEntries() {
    const entries = JSON.parse(localStorage.getItem('journalEntries')) || [];
    entriesList.innerHTML = '';
  
    entries.forEach((entry, index) => {
      const li = document.createElement('li');
      li.innerHTML = `
        <div>
          <strong>${entry.date}</strong>
          <p>${entry.text}</p>
        </div>
        <button class="deleteBtn" data-index="${index}">Delete</button>
      `;
      entriesList.appendChild(li);
    });
  
    document.querySelectorAll('.deleteBtn').forEach(btn =>
      btn.addEventListener('click', deleteEntry)
    );
  }

function deleteEntry(e) {
    if (!confirm('Delete this entry?')) return;
    const index = e.target.dataset.index;
    const entries = JSON.parse(localStorage.getItem('journalEntries')) || [];
  
    entries.splice(index, 1); // Remove the selected entry
    localStorage.setItem('journalEntries', JSON.stringify(entries));
    loadEntries();
  }