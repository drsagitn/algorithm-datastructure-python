// src/components/ThemeList.js
import React from 'react';

const ThemeList = ({ themes }) => {
  return (
    <div className="theme-list">
      {themes.map((theme) => (
        <div
          key={theme.id}
          className="theme-item uppercase align-middle"
        >
          {theme.title}
        </div>
      ))}
    </div>
  );
};

export default ThemeList;
