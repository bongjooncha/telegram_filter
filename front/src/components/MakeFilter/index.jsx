import style from "./makeFilter.module.css";
import ChatId from "components/ChatId";

function MakeFilter() {
  return (
    <div className={style.MakeFilter}>
      <div>Make Filter</div>
      <div>
        <div className={style.items}></div>
        <div className={style.chatrooms}>
          <ChatId />
        </div>
      </div>
    </div>
  );
}

export default MakeFilter;
