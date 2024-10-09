import style from "./index.module.css";

function Rooms({ rooms, setRooms, checkedIds }) {
  // 항목 추가
  const handleAddChecker = () => {
    const newRooms = [...rooms];
    checkedIds.forEach((checkedId) => {
      if (!newRooms.some((room) => room.id === checkedId.id)) {
        newRooms.push(checkedId);
      }
    });
    setRooms(newRooms);
  };
  // 항목 삭제
  const handleDeleteroom = (index) => {
    const updatedInputs = rooms.filter((_, i) => i !== index);
    setRooms(updatedInputs);
  };

  // 전체삭제
  const handleDeleteAll = () => {
    setRooms([]);
  };

  return (
    <div className={style.roomList}>
      <div className={style.inputsParents}>
        {rooms.map((word, index) => (
          <div className={style.inputs} key={index}>
            <input type="text" value={word.name} readOnly />
            <button
              className={style.inputButton}
              onClick={() => handleDeleteroom(index)}
            >
              삭제
            </button>
          </div>
        ))}
      </div>
      <div className={style.bottomButton}>
        <button className={style.addGroup} onClick={handleAddChecker}>
          add checked
        </button>
        <button className={style.deleteGroup} onClick={handleDeleteAll}>
          delete all
        </button>
      </div>
    </div>
  );
}

export default Rooms;
