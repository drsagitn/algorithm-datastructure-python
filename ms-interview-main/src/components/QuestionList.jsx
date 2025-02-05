// src/QuestionList.js
import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';

const QuestionList = ({ themes }) => {
  const [expandedQuestion, setExpandedQuestion] = useState(null);

  const toggleAnswer = (id) => {
    setExpandedQuestion(expandedQuestion === id ? null : id);
  };

  return (
    <div className="table ">
      {themes.map((theme) => (
        <div key={theme.id} className="table-row">
          {/* Theme Title Cell */}
          <div className="table-cell theme-cell">
            <span>{theme.title}</span>
          </div>
          {/* Questions and Answers Cell */}
          <div className="table-cell questions-cell">
            {theme.questions.map((question, index) => {
              const questionId = `${theme.id}-${index}`;
              return (
                <div key={questionId} className="question">
                  <h3 onClick={() => toggleAnswer(questionId)} className='font-bold'>{question.question}</h3>
                  {expandedQuestion === questionId && (
                    <ReactMarkdown className="answer bg-gray text-white">{question.answer}</ReactMarkdown>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      ))}
    </div>
  );
};

export default QuestionList;
