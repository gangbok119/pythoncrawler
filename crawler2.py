# 가장 최신화가 가장 앞에 있다는 가정하에 진행


"""
class NaverWebtoonCrawler생성
    초기화메서드
        webtoon_id
        episode_list (빈 list)
            를 할당

    인스턴스 메서드
        def get_episode_list(self, page)
            해당 페이지의 episode_list를 생성, self.episode_list에 할당

        def clear_episode_list(self)
            자신의 episode_list를 빈 리스트로 만듬

        def get_all_episode_list(self)
            webtoon_id의 모든 episode를 생성

        def add_new_episode_list(self)
            새로 업데이트된 episode목록만 생성

"""
import utils
import pickle
import os



class NaverWebtoonCrawler(): # 확장해서 그냥 웹툰 크롤러로 만들고, 크롤러 하나 내에 네이버/다음 등으로 가르려 하는 것.
    """docstring for """
    def __init__(self, webtoon_id):
        self.webtoon_id=webtoon_id
        self.episode_list=[]  # 에피소드들이 수정될 일이 없으므로 클래스의 기능을 겸하는 네임드 튜플을 사용
        self.load(init=True)
        # 수정이 힘들지만 연산량이 적으므로 더 편할 듯.
    # 객체 생성 시. 'db/{}.txt'.format(self.webtoon_id)가 존재하면
    # 바로 load()하도록 작성

    @property
    def get_total_episode_count(self):
        '''
        webtoon_id에 해당하는 실제 웹툰의 총 episode수를 리턴
        requests를 사용
        return: 총 episode수(int)
        '''
        el = utils.get_webtoon_episode_list(self.webtoon_id)
        return int(el[0].no)




    def update_episode_list(self, force_update=False):
        '''
        1. cur_recent_episode_no = self.episode_list에서 가장 최신화의 no
        2. while/for문 내부에서 page값을 늘려가며
         utils.get_webtoon_episode_list를 호출
         반환된 list(episode)들을 해당 episode의
         no가 recent_episode_no보다 클 때 까지만 self.episode_list에 추가


        self.episode_list에 존재하지 않는 episode들을 self.episode_list에 추가
        param force_update=True : 이미 존재하는 episode들도 강제로 업데이트
        return: 추가된 episode의 수(int)
        '''
        #self.episode_list - 비어 있는 경우 None을 주어야 하므로...
     #   recent_episode_no = self.episode_list[0].no if self.episode_list else None

    #    willpages=(self.get_total_episode_count - recent_episode_no)//10+1 if self.episode_list else willpages = self.get_total_episode_count//10+1
    #    for i in range(1,willpages+1):
    #        items=utils.get_webtoon_episode_list(self.webtoon_id,i)
    #       self.episode_list.insert(0,items)

        #변수 없이 break의 실행을 확인하는 방법 - for(순회가 참일때까지 - while+if) / else

        #올려주신 코드
        recent_episode_no = self.episode_list[0].no if self.episode_list else 0 #처음부터 끝까지 가져오는 경우
        print('- Update episode list start (Recent episode no: %s) -' % recent_episode_no)
        page = 1
        new_list = list()
        while True:
            print('  Get webtoon episode list (Loop %s)' % page)
            # 계속해서 증가하는 'page'를 이용해 다음 episode리스트들을 가져옴
            el = utils.get_webtoon_episode_list(self.webtoon_id, page)
            # 가져온 episode list를 순회
            for episode in el:
                # 각 episode의 no가 recent_episode_no보다 클 경우,
                # self.episode_list에 추가
                if int(episode.no) > int(recent_episode_no):
                    new_list.append(episode)
                    if int(episode.no) == 1:#첫화부터 끝까지 가져오는 경우를 위한 처리.
                        break
                else:
                    break
            # break가 호출되지 않았을 때
            else:
                # 계속해서 진행해야 하므로 page값을 증가시키고 continue로 처음으로 돌아감
                page += 1
                continue
            # el의 for문에서 break가 호출될 경우(더 이상 추가할 episode없음
            # while문을 빠져나가기위해 break실행
            break
        self.episode_list = new_list + self.episode_list
        return len(new_list) # 추가된 에피소드의 개수
        #정말 최신화만 가져왔는가?

    def get_last_page_episode_list(self):
        el = utils.get_webtoon_episode_list(self.webtoon_id, 99999) #url의 page 값은 해당 값 초과하면 자동으로 마지막 페이지
        self.episode_list = el
        return len(self.episode_list)
   # 무조건 1화가 있는 페이지에 있는 에피소드만 가져오게 됨.

    @property
    def up_to_date(self):
        '''
        현재 가지고 있는 episode_list가 웹상의 최신 episode까지 가지고 있는지
        return boolean값
        1. cur_episode_count = self.episode_list의 개수
        2. total_episode_count = 웹상의 총 episode 개수
        3. 위 두 변수의 값이 같으면 return True 아니면 return False


        '''
        #total_episode_count = self.get_total_episode_count
        #cur_episode_count = self.episode_list[0].no
        #return cur_episode_count == total_episode_count

        #지금 가지고 있는 총 episode의 개수
        # self.episode_list에 저장되어 있음
        # 리스트형 객체
        # 리스트형 객체의 길이를 구하는 함수(시퀀스형 객체는 모두 가능)
        # 내장함수 len(s)
        # 최신화인지/ 몇 화를 가지고 있는지 확인해야 함.

        #cur_episode_count = len(self.episode_list)

        #웹상의 총 episode갯수
        #total_episode_count = self.total_episode_count
        return len(self.episode_list) == self.total_episode_count
        #return cur_episode_count == total_episode_count


        #if el[0].no == self.episode_list[0].no:
        #    return True
        #else:
        #    return False


        #설명
        #최신 episode 1개를 가져와 Episode namedtuple로 만듦
        #self.episode_list의 첫 번째 값과 비교
        #같으면 최신화가 되어있음.


    def save(self, path=None):
        '''
        1.폴더 생성시
        os.is_dir(path)
        path가 디렉토리인지 확인

        os.mkdir(path)
        path의 디렉토리를 생성

        2. 저장시
        obj - object(모든 객체 가능)
        file - file object(파일 객체, bytes 형식으로 write 가능한)
        pickle.dump(obj, file)

        현재폴더를 기준으로 db/<webtoon_id>.txt 파일에 pickle로 self.episode_list를 저장
        return 성공여부
        '''

        #  with open('db/<{}>.txt'.format(self.webtoon_id),'wb') as f:
        #      os.mkdir('db')
        #      os.is_dir('db')
        #      os.chdir('db')
        #      pickle.dump(self.episode_list,f)
        #      os.chdir('../')
        #  return None

        # 이 폴더 기준으로 db 폴더가 있는지 검사 후 없으면 만들기
        if not os.path.isdir('db'):
            os.mkdir('db')
        # obj = self.episode_list
        # path = 'db/%s.txt' % self.webtoon_id

        pickle.dump(self.episode_list, open( 'db/%s.txt' % self.webtoon_id,'wb'))



    def load(self, path=None, init=False):
        #처음 인스턴스를 생성할 때, FileNotFoundError를 띄우지 않으려는 것.
        '''
        현재폴더를 기준으로 db/<webtoon_id>.txt 파일의 내용을 불러와
        pickle로 self.episode_list를 복원

        1. 만약 db 폴더가 없으면 or db/webtoon_id_txt파일이 없으면
        -> "불러올 파일이 없습니다." 출력

        2. 있으면 복원

        '''
        #if os.path.exists('db/{}.txt'.format(self.webtoon_id)):
        #    pickle.load(self.episode_list, open('db/%s.txt' % self.webtoon_id,'rb'))
        #else:
        #    print('불러올 파일이 없습니다.')

        #혹은

        try:
            path = 'db/{}.txt'.format(self.webtoon_id)
            obj = pickle.load(open(path,'rb'))
            self.episode_list = obj
        except FileNotFoundError:
            if not init: # init(초기화메서드에서 불러온 게 아니라면 실행)
                print('불러올 파일이 없습니다.')